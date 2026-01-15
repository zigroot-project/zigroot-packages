# Registry Package: linux-rockchip-rv110x

This package provides the Linux kernel for Rockchip RV1106/RV1103 SoCs (Luckfox Pico boards).

## Files for zigroot-project/zigroot-packages

Copy these to `packages/linux-rockchip-rv110x/` in the zigroot-packages repository:

```
packages/linux-rockchip-rv110x/
├── metadata.toml
├── 6.6.0.toml
└── patches/
    ├── luckfox-pico-6.6-support.patch
    └── luckfox-6.6-fixes.patch
```

## Patches

The patches add:
1. `luckfox-pico-6.6-support.patch` - Device tree support for all Luckfox Pico variants
2. `luckfox-6.6-fixes.patch` - Build fixes for kernel 6.6 on RV1106
