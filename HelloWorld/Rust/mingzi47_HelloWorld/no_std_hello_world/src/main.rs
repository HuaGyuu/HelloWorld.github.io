#![no_std]
#![no_main]

const UART0: *mut u8 = 0x1000_0000 as *mut u8;
const EXIT_ADDR: u64 = 0x100000;
const EXIT_CODE: u64 = 0x5555;

static HELLO: &[&[u8]] = &[
    b"\n",
    // red
    b"\x1b[31m",
    // Hello World
    b"88  88 888888 88     88      dPYb Yb        dP dPYb  88\"\"Yb 88     8888b\n",
    b"88  88 88__   88     88     dP  Yb Yb  db  dP dP  Yb 88__dP 88     8I  Yb\n",
    b"888888 88\"\"   88  .o 88  .o Yb  dP  YbdPYbdP  Yb  dP 88\"Yb  88  .o 8I  dY\n",
    b"88  88 888888 88ood8 88ood8  YboP    YP  YP    YboP  88  Yb 88ood8 8888Y\"\n",
    // color end
    b"\x1b[0m",
];

// main
#[unsafe(no_mangle)]
pub extern "C" fn _start() -> ! {
    for line in HELLO {
        line.iter()
            .for_each(|&c| {
                unsafe {
                    // output
                    UART0.write_volatile(c);
                }
            });
    }

    // exit qemu
    exit!(EXIT_CODE);
}

use core::panic::PanicInfo;

// no std, must impl 
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    exit!(EXIT_CODE);
}

#[macro_export]
macro_rules! exit {
    ($exit_code: expr) => {
        {
            unsafe {
                core::arch::asm!(
                    "sw {0}, 0({1})",
                    in(reg)$exit_code, in(reg)EXIT_ADDR,
                )
            }

            loop {
                unsafe {
                    core::arch::asm!(
                        "wfi",
                        options(nomem, nostack)
                    );
                }
            }
        }
    };
}
