variable board 8 allot
board 9 0 fill
variable turn
1 turn !

: output-player ( player -- )
case
0 of ." . " endof
1 of ." X " endof
2 of ." O " endof
     ." ? "
endcase ;

: output-board 9 0 do board i + c@ output-player i 3 mod 2 = if cr then loop ;
: output page output-board turn c@ output-player ." to play " cr ;
: output-victory page output-board turn c@ output-player ." wins " cr ;
: output-draw page output-board ." cat's game " cr ;

: ascii-to-pos ( ascii -- pos )
case
113 ( q ) of 0 endof
119 ( w ) of 1 endof
101 ( e ) of 2 endof
97  ( a ) of 3 endof
115 ( s ) of 4 endof
100 ( d ) of 5 endof
122 ( z ) of 6 endof
120 ( x ) of 7 endof
99  ( c ) of 8 endof
             -1
endcase ;

: swap-turn turn @ 2 mod 1 + turn ! ;
: set-cell ( n v -- ) swap board + c! ;
: cell-empty? ( n -- e? ) board + c@ 0 = ;

: do-move ( pos -- ) turn c@ set-cell swap-turn ;
: try-move ( pos -- ) dup cell-empty? if do-move else drop then ;

: get-input ( -- pos ) key ascii-to-pos ;
: try-input ( -- ) get-input dup -1 <> if try-move else drop then ;

: 3check ( a b c -- win? ) over = rot rot over = rot and swap 0 <> and ; 

: ?victory ( -- v? )
board     c@ board 3 + c@ board 6 + c@ 3check
board 1 + c@ board 4 + c@ board 7 + c@ 3check or
board 2 + c@ board 5 + c@ board 8 + c@ 3check or
board     c@ board 1 + c@ board 2 + c@ 3check or
board 3 + c@ board 4 + c@ board 5 + c@ 3check or
board 6 + c@ board 7 + c@ board 8 + c@ 3check or
board     c@ board 4 + c@ board 8 + c@ 3check or
board 2 + c@ board 4 + c@ board 6 + c@ 3check or
;

: ?draw ( -- d? ) 1 9 0 do board i + c@ 0 <> and loop ;
: ?game-end ( -- e? ) ?victory ?draw or ;
: show-end ?victory if swap-turn output-victory else output-draw then ;

: reset-board 9 0 do 0 board i + c! loop ;
: reset-turn 1 turn c! ;
: reset-game reset-board reset-turn ;

: game begin output try-input ?game-end until show-end ;
: replay-loop begin reset-game game ." play again? (y/n) " cr key 121 <> until bye ;

replay-loop
