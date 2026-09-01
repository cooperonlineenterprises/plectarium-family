# Embedded Related Packets

This directory contains the validated **UCA Full Product Build Packet v1** as the family's first detailed reference implementation.

## Files

- `uca-full-product-build-packet-v1.zip` — independently validated UCA product constitution, executable specification, and AI build packet.
- `uca-full-product-build-packet-v1.manifest.json` — the embedded packet's own manifest.
- `uca-full-product-build-packet-v1.zip.sha256` — SHA-256 of the embedded archive.

## Authority

The embedded UCA packet is authoritative for UCA-specific architecture. The family packet may identify broader shared patterns, but it MUST NOT silently weaken or supersede established UCA decisions. Shared conventions remain provisional unless promoted through the family decision process after evidence from additional capability implementations.

## Integrity

The family validator checks that the embedded ZIP is readable and that its SHA-256 matches the adjacent digest file. UCA's own validator remains authoritative for its internal contents.
