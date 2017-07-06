#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_mouse;
uniform vec2 u_resolution;
uniform float u_time;

uniform sampler2D u_tex0;
uniform vec2 u_tex0Resolution;

varying vec4 v_position;
varying vec4 v_color;
varying vec3 v_normal;
varying vec2 v_texcoord;

mat2 rotate2d(float _angle){
    return mat2(cos(_angle),-sin(_angle),
                sin(_angle),cos(_angle));
}

mat2 scale2d(vec2 _scale){
    return mat2(_scale.x,0.0,
                0.0,_scale.y);
}

void main (void) {
  vec2 p = vec2(v_position.x, v_position.y) * rotate2d(u_time) * scale2d(sin(vec2(u_time, u_time)/10.0)*10.0);
  gl_FragColor = vec4(sin(p.y*3.14) * sin(p.x*3.14), 0.0, 0.0, 1.0);
}
