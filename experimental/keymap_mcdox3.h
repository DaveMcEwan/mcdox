/*
Ideas/planning for mcdox3
=========================================================================

- Reduced keypad vs mcdox1 (Ergodox-compatible) and mcdox2 (two fewer keys).
-

Keymap 0: Default Layer
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  |  Esc  |   '   |   ,   |   .   |   P   |   Y   |               |   F   |   G   |   C   |   R   |   L   |   =   |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  |  Tab  |   A   |   O   |   E   |   U   |   I   |               |   D   |   H   |   T   |   N   |   S   |   -   |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  |  BkSp |   ;   |   Q   |   J   |   K   |   X   |               |   B   |   M   |   W   |   V   |   Z   |   /   |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
          | Home  | PgDn  | PgUp  | End   |                               | Left  |  Up   |  Dn   | Right |
          +-------+-------+-------+-------+                               +-------------------------------+
                              +-------+-------+-------+       +-------+-------+-------+
                              | LShft | LCtrl |  ~L1  |       |  ~L2  | Enter | Space |
                              +-------+-------+-------+       +-------+-------+-------+

Keymap 1: Left-Toggle Layer
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  | trns  |   !   |   @   |   #   |   $   |   %   |               |   ^   |   &   |   *   |   (   |   )   | trns  |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  | trns  |   1   |   2   |   3   |   4   |   5   |               |   6   |   7   |   8   |   9   |   0   | trns  |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  | trns  |   \   |   |   |   `   |   ~   | LAlt  |               | RAlt  |   {   |   }   |   [   |   ]   | trns  |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
          |  FN1  |  FN2  |  FN3  |  FN4  |                               | trns  | trns  | trns  | trns  |
          +-------+-------+-------+-------+                               +-------------------------------+
                              +-------+-------+-------+       +-------+-------+-------+
                              | trns  | trns  |  N/A  |       |  Nop  | RCtrl |  Del  |
                              +-------+-------+-------+       +-------+-------+-------+

Keymap 2: Right-Toggle Layer
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  | trns  |  F1   |  F2   |  F3   |  F4   |  F5   |               |  F6   |  F7   |  F8   |  F9   |  F10  | trns  |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  | trns  |  F11  |  F12  | PrtSc | Mute  | Vol-  |               | Vol+  | ClkL  | ClkM  | ClkR  |  Nop  | trns  |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  | trns  |  FN5  |  FN6  |  FN7  |  App  | LGui  |               | RGui  |  MsL  |  MsU  |  MsD  |  MsR  | trns  |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
          | ScrL  | ScrU  | ScrD  | ScrR  |                               | trns  | trns  | trns  | trns  |
          +-------+-------+-------+-------+                               +-------------------------------+
                              +-------+-------+-------+       +-------+-------+-------+
                              | trns  | trns  |  Nop  |       |  N/A  | Enter |  Ins  |
                              +-------+-------+-------+       +-------+-------+-------+

FN ideas:
    - passwordA,
    - passwordB,
    - GBP symbol in Vim,
    - toggle sticky L1/L2 layers,
    - sticky Greek layer,
    - sticky Inkscape layer,
    - sticky KiCad layer,
    - run test routine,
    - Nop,

Keymap N: Blank Template
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  |       |       |       |       |       |       |               |       |       |       |       |       |       |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  |       |       |       |       |       |       |               |       |       |       |       |       |       |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
  |       |       |       |       |       |       |               |       |       |       |       |       |       |
  +-------+-------+-------+-------+-------+-------+               +-------+-------+-------+-------+-------+-------+
          |       |       |       |       |                               |       |       |       |       |
          +-------+-------+-------+-------+                               +-------------------------------+
                              +-------+-------+-------+       +-------+-------+-------+
                              |       |       |       |       |       |       |       |
                              +-------+-------+-------+       +-------+-------+-------+
*/

/* mcdox3 keymap definition macro */
#define KEYMAP(                                      \
  k00,k01,k02,k03,k04,k05,  k06,k07,k08,k09,k0A,k0B, \
  k10,k11,k12,k13,k14,k15,  k16,k17,k18,k19,k1A,k1B, \
  k20,k21,k22,k23,k24,k25,  k26,k27,k28,k29,k2A,k2B, \
      k31,k32,k33,k34,          k37,k38,k39,k3A    , \
              k43,k44,k45,  k46,k47,k48            ) \
 {                                                   \
  {KC_##k00,KC_##k01,KC_##k02,KC_##k03,KC_##k04,KC_##k05,  KC_##k06,KC_##k07,KC_##k08,KC_##k09,KC_##k0A,KC_##k0B},   \
  {KC_##k10,KC_##k11,KC_##k12,KC_##k13,KC_##k14,KC_##k15,  KC_##k16,KC_##k17,KC_##k18,KC_##k19,KC_##k1A,KC_##k1B},   \
  {KC_##k20,KC_##k21,KC_##k22,KC_##k23,KC_##k24,KC_##k25,  KC_##k26,KC_##k27,KC_##k28,KC_##k29,KC_##k2A,KC_##k2B},   \
  {KC_NO   ,KC_##k31,KC_##k32,KC_##k33,KC_##k34,KC_NO   ,  KC_NO   ,KC_##k37,KC_##k38,KC_##k39,KC_##k3A,KC_NO   },   \
  {KC_NO   ,KC_NO   ,KC_NO   ,KC_##k43,KC_##k44,KC_##k45,  KC_##k46,KC_##k47,KC_##k48,KC_NO   ,KC_NO   ,KC_NO   },   \
 }
// NOTE: mcdox1 has rows/columns swapped, so this macro could do the transpose.
// {                                                  \
//  {KC_##k00,KC_##k10,KC_##k20,KC_NO   ,KC_NO   },   \
//  {KC_##k01,KC_##k11,KC_##k21,KC_##k31,KC_NO   },   \
//  {KC_##k02,KC_##k12,KC_##k22,KC_##k32,KC_NO   },   \
//  {KC_##k03,KC_##k13,KC_##k23,KC_##k33,KC_##k43},   \
//  {KC_##k04,KC_##k14,KC_##k24,KC_##k34,KC_##k44},   \
//  {KC_##k05,KC_##k15,KC_##k25,KC_NO   ,KC_##k45},   \
//  {KC_##k06,KC_##k16,KC_##k26,KC_NO   ,KC_##k46},   \
//  {KC_##k07,KC_##k17,KC_##k27,KC_##k37,KC_##k47},   \
//  {KC_##k08,KC_##k18,KC_##k28,KC_##k38,KC_##k48},   \
//  {KC_##k09,KC_##k19,KC_##k29,KC_##k39,KC_NO   },   \
//  {KC_##k0A,KC_##k1A,KC_##k2A,KC_##k3A,KC_NO   },   \
//  {KC_##k0B,KC_##k1B,KC_##k2B,KC_NO   ,KC_NO   },   \
// }

static const uint8_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
  KEYMAP(
     ESC  , QUOT  , COMM  ,  DOT  ,   P   ,   Y   ,                   F   ,   G   ,   C   ,   R   ,   L   ,  EQL  ,
     TAB  ,   A   ,   O   ,   E   ,   U   ,   I   ,                   D   ,   H   ,   T   ,   N   ,   S   , MINS  ,
    BSPC  , SCLN  ,   Q   ,   J   ,   K   ,   X   ,                   B   ,   M   ,   W   ,   V   ,   Z   , SLSH  ,
            HOME  , PGDN  , PGUP  ,  END  ,                                 LEFT  ,  UP   , DOWN  , RGHT  ,
                        LSFT  , LCTL  ,  FN1  ,                  FN2  ,  ENT  , SPC
  ),

  KEYMAP(
    TRNS  , S(1)  , S(2)  , S(3)  , S(4)  , S(5)  ,                 S(6)  , S(7)  , S(8)  , S(9)  , S(0)  , TRNS  ,
    TRNS  ,   1   ,   2   ,   3   ,   4   ,   5   ,                   6   ,   7   ,   8   ,   9   ,   0   , TRNS  ,
    TRNS  , BSLS  ,S(BSLS),  GRV  ,S(GRV) , LALT  ,                 RALT  ,S(LBRC),S(RBRC), LBRC  , RBRC  , TRNS  ,
             FN1  ,  FN2  ,  FN3  ,  FN4  ,                                 TRNS  , TRNS  , TRNS  , TRNS  ,
                        TRNS  , TRNS  , TRNS  ,                   NO  , RCTL  , DEL
  ),

  KEYMAP(
    TRNS  ,  F1   ,  F2   ,  F3   ,  F4   ,  F5   ,                  F6   ,  F7   ,  F8   ,  F9   ,  F10  , TRNS  ,
    TRNS  ,  F11  ,  F12  , PSCR  , MUTE  , VOLD  ,                 VOLU  , BTN1  , BTN3  , BTN2  ,  NO   , TRNS  ,
    TRNS  ,  FN5  ,  FN6  ,  FN7  ,  APP  , LGUI  ,                 RGUI  , MS_L  , MS_U  , MS_D  , MS_R  , TRNS  ,
            WH_L  , WH_U  , WH_D  , WH_R  ,                                 TRNS  , TRNS  , TRNS  , TRNS  ,
                        TRNS  , TRNS  ,  NO   ,                 TRNS  ,  ENT  , INS
  ),
};

/*
 * Fn action definition
 */
static const uint16_t PROGMEM fn_actions[] = {
    ACTION_FUNCTION(TEENSY_KEY),                    // FN0 - Teensy key
    ACTION_LAYER_MOMENTARY(1),                      // FN1 - Momentary Layer1
    ACTION_LAYER_MOMENTARY(2),                      // FN2 - Momentary Layer2
    ACTION_MACRO(0),                                // FN3 - Password0
};

