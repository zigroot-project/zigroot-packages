# U-Boot for Rockchip RV1106/RV1103

U-Boot bootloader for Rockchip RV1106 and RV1103B SoCs, based on the Luckfox SDK.

## Supported Hardware

- Luckfox Pico (RV1106)
- Luckfox Pico Plus (RV1106)
- Luckfox Pico Pro/Max (RV1106)
- RV1103B-based boards

## Options

### `defconfig`

| Value | Boot Media | Mode | Use Case |
|-------|-----------|------|----------|
| `luckfox_rv1106_uboot` (default) | SD + eMMC + SPI NAND | Full | Development |
| `luckfox_rv1106_uboot_emmc_tb` | eMMC | TinyBoot | Production (eMMC) |
| `luckfox_rv1106_spi_nand_tb` | SPI NAND | TinyBoot | Production (SPI NAND) |

### `soc`

| Value | Description |
|-------|-------------|
| `rv1106` (default) | RV1106 SoC (Luckfox Pico series) |
| `rv1103b` | RV1103B SoC variant |

## Defconfig Comparison

| Feature | `luckfox_rv1106_uboot` | `*_emmc_tb` | `*_spi_nand_tb` |
|---------|:----------------------:|:-----------:|:---------------:|
| SD card boot | ✅ | ❌ | ❌ |
| eMMC boot | ✅ | ✅ | ❌ |
| SPI NAND boot | ✅ | ❌ | ✅ |
| Network (TFTP/DHCP) | ✅ | ❌ | ❌ |
| GPIO commands | ✅ | ❌ | ❌ |
| FAT filesystem | ✅ | ❌ | ❌ |
| SD card update | ✅ | ❌ | ❌ |
| A/B partitions | ✅ | ❌ | ❌ |
| Fast boot | ❌ | ✅ | ✅ |

**TinyBoot (TB)** variants skip full U-Boot and boot the kernel directly from SPL for faster boot times. Use for production devices.

## Required Blobs

The bootloader requires proprietary DDR initialization and SPL blobs from Rockchip:

| SoC | DDR Blob | SPL Blob |
|-----|----------|----------|
| RV1106 | `rv1106_ddr_924MHz_v1.15.bin` | `rv1106_spl_v1.02.bin` |
| RV1103B | `rv1103b_ddr_924MHz_v1.05.bin` | `rv1103b_spl_v1.00.bin` |

These are automatically downloaded from [rockchip-linux/rkbin](https://github.com/rockchip-linux/rkbin).

## Build Output

The build produces an `idblock.img` which combines DDR + SPL blobs, plus `uboot.img`.
