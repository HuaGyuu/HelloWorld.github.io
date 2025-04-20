# Makefile
TARGET := riscv64gc-unknown-none-elf
BIN_NAME := no_std_hello_world
QEMU_CMD := qemu-system-riscv64

env:
	(rustup target list | grep "riscv64gc-unknown-none-elf (installed)") || rustup target add $(TARGET)
	cargo install cargo-binutils
	rustup component add rust-src
	rustup component add llvm-tools-preview

build: env
	cargo build \
		--target $(TARGET) \
		--release \
		--target-dir ./target

objcopy: build
	rust-objcopy \
		--strip-all \
		-O binary \
		"target/$(TARGET)/release/$(BIN_NAME)" \
		"target/$(TARGET)/release/$(BIN_NAME).bin"

run: objcopy
	$(QEMU_CMD) \
		-machine virt \
		-m 128M \
		-nographic \
		-bios default \
		-kernel "target/$(TARGET)/release/$(BIN_NAME).bin" \

clean:
	cargo clean

.PHONY: build bin run clean env
