#![feature(slice_patterns)]
#![feature(inclusive_range_syntax)]

//TODO(Wesley) Remove allows
#![cfg_attr(feature="clippy", feature(plugin))]
#![allow(unused_variables)]
#![allow(dead_code)]

use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::Cursor;

extern crate byteorder;
use byteorder::{BigEndian, LittleEndian, ReadBytesExt};

#[derive(Debug)]
enum ElfType {
    NONE,
    RELOCATABLE,
    EXECUTABLE,
    SHARED,
    CORE,
    LOOS,
    HIOS,
    LOPROC,
    HIPROC
}

#[derive(Debug)]
enum ElfVersion {
    NONE,
    CURRENT
}

#[derive(Debug)]
enum ElfClass {
    NONE,
    BITS32,
    BITS64
}

#[derive(Debug)]
enum Abi {
    NONE,
    HPUX,
    NETBSD,
    GNU,
    SOLARIS,
    AIX,
    IRIX,
    FREEBSD,
    TRU64,
    MODESTO,
    OPENBSD,
    OPENVMS,
    NSK,
    AROS,
    FENIXOS,
    CLOUDAbi,
    OPENVOS
}

#[derive(Debug)]
enum SectionType {
    NULL,
    PROGBITS,
    SYMTAB,
    STRTAB,
    RELA,
    HASH,
    DYNAMIC,
    NOTE,
    NOBITS,
    REL,
    SHLIB,
    DYNSYM,
    INIT_ARRAY,
    FINI_ARRAY,
    PREINIT_ARRAY,
    GROUP,
    SYMTAB_INDEX,
    LOOS,
    HIOS,
    LOPROC,
    HIPROC,
    LOUSER,
    HIUSER
}

#[derive(Debug)]
enum SectionFlag {
    WRITE,
    ALLOC,
    EXECINSTR,
    MERGE,
    STRINGS,
    INFO_LINK,
    LINK_ORDER,
    OS_NONCONFORMING,
    GROUP,
    TLS,
    COMPRESSED,
    MASKOS,
    MASKPROC
}

#[derive(Debug)]
enum SectionInfo {
    DYNAMIC,
    HASH,
    REL,
    RELA,
    SYMTAB,
    DYNSYM,
    GROUP,
    SYMTAB_SHNDX
}

#[derive(Debug)]
struct Blob {
    data: Vec<u8>
}

#[derive(Debug)]
struct Section {
    name: String,
    section_type: SectionType,
    flags: Vec<SectionFlag>,
    addr: usize,
    data: Blob,
    link: SectionInfo,
    info: SectionInfo,
    addralign: usize,
    entsize: usize,
}

#[derive(Debug)]
enum SegmentType {
    NULL,
    LOAD,
    DYNAMIC,
    INTERP,
    NOTE,
    SHLIB,
    PHDR,
    TLS,
    LOOS,
    HIOS,
    LOPROC,
    HIPROC
}

#[derive(Debug)]
enum SegmentFlags {
    EXECUTE,
    WRITE,
    READ,
    MASKOS,
    MASKPROC
}

#[derive(Debug)]
struct Segment {
    segment_type: SegmentType,
    flags: Vec<SegmentFlags>,
    data: Blob,
    virt_addr: usize,
    physical_addr: usize,
    file_size: usize,
    memory_size: usize,
    align: usize
}

#[derive(Debug)]
enum ElfEncoding {
    NONE,
    DATA2LSB,
    DATA2MSB
}

//TODO(Wesley) Have ELFHeader actually represent the header, and use a different struct to
//represent the entire file.
#[derive(Debug)]
struct ElfHeader {
    class: ElfClass,
    encoding: ElfEncoding, //TODO: Actually use this
    abi: Abi,
    abi_version: u8,
    elf_type: ElfType,
    machine: u16, // I should use an enum for this, but I'm too damn lazy
    version: ElfVersion,
    entrypoint: usize, // not sure
    program_headers: Vec<Segment>,
    section_headers: Vec<Section>,
    flags: Vec<u8>
}

fn parse_section(bytes: &Vec<u8>, start: u64, size: u16) -> Section {
    //let name
    let section_type: SectionType = match Cursor::new(&bytes[(start + 4) as usize .. (start + 8) as usize]).read_u32::<LittleEndian>().unwrap() {
        1 => SectionType::PROGBITS,
        2 => SectionType::SYMTAB,
        3 => SectionType::STRTAB,
        4 => SectionType::RELA,
        5 => SectionType::HASH,
        6 => SectionType::DYNAMIC,
        7 => SectionType::NOTE,
        8 => SectionType::NOBITS,
        9 => SectionType::REL,
        10 => SectionType::SHLIB,
        11 => SectionType::DYNSYM,
        14 => SectionType::INIT_ARRAY,
        15 => SectionType::FINI_ARRAY,
        16 => SectionType::PREINIT_ARRAY,
        17 => SectionType::GROUP,
        18 => SectionType::SYMTAB_INDEX,
        0x60000000 => SectionType::LOOS,
        0x6fffffff => SectionType::HIOS,
        0x70000000 => SectionType::LOPROC,
        0x7fffffff => SectionType::HIPROC,
        0x80000000 => SectionType::LOUSER,
        0x8fffffff => SectionType::HIUSER,
        _ => SectionType::NULL
    };
    unimplemented!();
}

fn parse_segment(bytes: &Vec<u8>, start: u64, size: u16) -> Segment {
    unimplemented!();
}

fn parse_elf(bytes: Vec<u8>) -> ElfHeader {
    //TODO(Wesley) Parse ELF header in seperate function
    //TODO(Wesley) Add real support for reading 32bit ELF files
    if &bytes[0 .. 4] != [0x7f, 0x45, 0x4c, 0x46] {
        panic!("Wrong magic number, aborting!");
    }
    let class: ElfClass = match bytes[4] {
        1 => ElfClass::BITS32,
        2 => ElfClass::BITS64,
        _ => ElfClass::NONE
    };
    let encoding: ElfEncoding = match bytes[5] {
        1 => ElfEncoding::DATA2LSB,
        2 => ElfEncoding::DATA2MSB,
        _ => ElfEncoding::NONE
    };
    let version: ElfVersion = match bytes[6] {
        1 => ElfVersion::CURRENT,
        _ => ElfVersion::NONE
    };
    let abi: Abi = match bytes[7] {
        1 => Abi::HPUX,
        2 => Abi::NETBSD,
        3 => Abi::GNU,
        6 => Abi::SOLARIS,
        7 => Abi::AIX,
        8 => Abi::IRIX,
        9 => Abi::FREEBSD,
        10 => Abi::TRU64,
        11 => Abi::MODESTO,
        12 => Abi::OPENBSD,
        13 => Abi::OPENVMS,
        14 => Abi::NSK,
        15 => Abi::AROS,
        16 => Abi::FENIXOS,
        17 => Abi::CLOUDAbi,
        18 => Abi::OPENVOS,
        _ => Abi::NONE
    };
    let abi_version: u8 = bytes[8];
    let elf_type: ElfType = match bytes[16 ... 17] {
        [0x01, 0x00] => ElfType::RELOCATABLE,
        [0x02, 0x00] => ElfType::EXECUTABLE,
        [0x03, 0x00] => ElfType::SHARED,
        [0x04, 0x00] => ElfType::CORE,
        [0xfe, 0x00] => ElfType::LOOS,
        [0xfe, 0xff] => ElfType::HIOS,
        [0xff, 0x00] => ElfType::LOPROC,
        [0xff, 0xff] => ElfType::HIPROC,
        _ => ElfType::NONE
    };
    //TODO(Wesley) Do endianess right
    //TODO(Wesley) Switch to using hexidecimal for indices
    let machine = Cursor::new(&bytes[18 ... 19]).read_u16::<LittleEndian>().unwrap();
    let entrypoint = Cursor::new(&bytes[24 ... 31]).read_u64::<LittleEndian>().unwrap();
    let flags: Vec<u8> = bytes[32 ... 36].to_vec();

    let section_start = Cursor::new(&bytes[40 ... 47]).read_u64::<LittleEndian>().unwrap();
    let section_header_size = Cursor::new(&bytes[58 ... 59]).read_u16::<LittleEndian>().unwrap();
    let num_sections = Cursor::new(&bytes[60 ... 61]).read_u16::<LittleEndian>().unwrap();

    let mut sections: Vec<Section> = vec![];

    for i in 0 .. num_sections {
        sections.push(parse_section(&bytes, section_start + (section_header_size * i) as u64, section_header_size));
    }

    let segment_start = Cursor::new(&bytes[32 ... 48]).read_u64::<LittleEndian>().unwrap();
    let segment_header_size = Cursor::new(&bytes[54 ... 55]).read_u16::<LittleEndian>().unwrap();
    let num_segments = Cursor::new(&bytes[56 ... 57]).read_u16::<LittleEndian>().unwrap();

    let mut segments: Vec<Segment> = vec![];

    for i in 0 .. num_segments {
        segments.push(parse_segment(&bytes, segment_start + (segment_header_size * i) as u64, segment_header_size));
    }

    unimplemented!();
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let mut file = File::open(&args[1]).expect("File not found!");
    let mut contents: Vec<u8> = vec![];
    file.read_to_end(&mut contents).expect("Failed to read file!");
    parse_elf(contents);
}
