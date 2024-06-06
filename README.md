# Creation IDs
Creation IDs are used to digitally identify unique creations of many forms. The term **creation** is intentionally vague to encompass anything digitally identifiable. Creation IDs can be used in any system that needs a standard creation identifier such as BLE device discovery, WiFi device identification or FPGA peripheral identification.

Creation IDs are administered by a person or organization who has been assigned a **creator** ID. They may or may not actually be the creator of the creation. Creator IDs are 32-bit numbers administered in this repository and are paired with 32-bit creation ids that are administered by the creator. These are similar to USB vendor ID (VID) and product ID (PID) but open source and freely available.

## Getting a new creator ID
Creator IDs are 32-bit numbers that designate who created something. In practice, this may also designate a third-party who is maintaining IDs on the behalf of the creator. For example, creator IDs automatically encompass all 16-bit USB vendor IDs by prepending the 16-bit `0x0000` prefix. Creator and creation IDs use `_` to separate the 16-bit halves to make these prefixes more obvious. We also have the `0x000C` prefix for community administered creation IDs for creators with an existing USB VID.

### For your own creations
Make a change to this README and make a PR to get a new creator ID for your own creations. If you have your own USB VID already, add an entry with the `0x0000` prefix and link to the location of your creation IDs. If not, choose a unique 32-bit number that doesn't start with `0x00` because that is reserved for other ID subsets.

### For someone else's creations
Make a change to this README and make a PR to document it. If the creator has a USB VID assigned to them, then add an entry with the `0x000C` prefix to denote that it is community administered. If not, choose a unique 32-bit number that doesn't start with `0x00` because that is reserved for other ID subsets. The complete list of USB Vendor IDs is available from the [USB Developers](https://usb.org/developers) page under "Valid USB Vendor ID Numbers". We're ok using obsolete VIDs as well because they are still unique.

It is often the case that community creation ids will also be administered in this repo as well. If that's what you want to do, then also add a `creations/<creator>.md` file in your PR. You can also create a separate place to administer creation ids so that you control who can assign them. We don't care as long as the creation id is unique and makes that clear.

## Allocating a new creation ID
Creation ID allocation is left up to the creator. However, here are some guidelines for consistency.

1. If the creator has a USB VID and the creation is a product with a USB PID, then use the `0x0000` prefix plus the USB PID for the creation id.
2. If the creation doesn't use USB or doesn't have a unique USB PID, then use a prefix that isn't `0x0000` (to reserve it for USB PIDs.)
3. Use the 16-bit prefix to group creations. For example, Espressif development boards usually have a chip specific prefix such as `0x00C3`.

# Assigned Creator IDs

## `0x0000_xxxx` - Reserved for USB VID IDs and official allocations

* `0x0000_0000` [Reserved](https://github.com/creationid/creators)
* `0x0000_239A` [Adafruit](https://github.com/adafruit/adafruit-creations)
* `0x0000_303A` [Espressif](https://github.com/espressif/usb-pids)

## `0x000C_xxxx` - Reserved for USB VID IDs administered by the community

* `0x000C_2886` [Seeed Studio](./creations/seeed-studio.md)
* `0x000C_303A` [Espressif](./creations/espressif.md)
* `0x000C_303B` [AI Thinker](./creations/ai-thinker.md)

## `0x00xx_xxxx` - Reserved for future ID subsets

## `0x01xx_xxxx`
* `0x0101_1ACE` [01 Space](./creations/01space.md)

## `0x0Dxx_xxxx`
* `0x0D10_C000` [VIDI](./creations/vidi.md)
* `0x0D10_D000` [Hardkernel](./creations/hardkernel.md)
* `0x0DB6_ED6E` [Debug Edge](https://debug-edge.io)

## `0x1xxx_xxxx`
* `0x1010_1010` [DFRobot](./creations/dfrobot.md)
* `0x1011_1011` [WeAct](./creations/weact.md)
* `0x1015_1015` [M5Stack](./creations/m5stack.md)
* `0x1337_1337` [Mark Olsson (k0d)](https://github.com/k0d)
* `0x148E_173C` [Heltec](./creations/heltec.md)
* `0x1876_0000` [Spotpear](./creations/spotpear.md)
* `0x1923_1923` [Deneyap](./creations/deneyap.md)
* `0x1988_1988` [Wemos](./creations/wemos.md)
* `0x1996_0000` [Silabs](./creations/silabs.md)
* `0x1998_1000` [Maker Go](./creations/makergo.md)
* `0x1999_1000` [Sunton](./creations/sunton.md)
* `0x1A00_0000` [Makerfabs](./creations/makerfabs.md)
* `0x1BBB_0000` [Waveshare](./creations/waveshare.md)
* `0x1C33_0000` [Freenove](./creations/freenove.md)

## `0x4xxx_xxxx`

* `0x4496_E3F4` [SQFMI](./creations/sqfmi.md)
* `0x4D69_0000` [Oak Dev Tech](creations/oakdevtech.md)
* `0x4F58_3097` [Oxocard](creations/oxocard.md)

## `0x6xxx_xxxx`
* `0x6d44_6576` [MicroDev](https://github.com/microdev1)

## `0x7xxx_xxxx`
* `0x7001_0001` [Bruce Segal (skieast)](https://github.com/skieast)

## `0xBxxx_xxxx`
* `0xB0B0_0000` [Unexpected Maker](https://github.com/unexpectedmaker)
* `0xBA00_0000` [Espruino / Bangle.js](./creations/espruino.md)

## `0xCxxx_xxxx`
* `0xC3C3_0000` [LILYGO](./creations/lilygo.md)

## `0xDxxx_xxxx`
* `0xDEAD_BEEF` [Luatos](./creations/luatos.md)
* `0xD03E_0000` [DoHome](./creations/dohome.md)
