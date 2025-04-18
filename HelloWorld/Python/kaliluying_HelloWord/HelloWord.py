# ASCII码转换
chars = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
print(''.join(chr(c) for c in chars))

# 彩虹色效果 (需支持ANSI的终端)
print("\033[31mH\033[32me\033[33ml\033[34ml\033[35mo\033[36m \033[35mW\033[34mo\033[33mr\033[32ml\033[31md\033[0m")

# 打字机效果
import time

text = "Hello World"
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)
print()

# 摩尔斯电码
reverse_morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z', '/': ' '}

morse_str = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
decoded_text = ''.join(reverse_morse.get(code, '') for code in morse_str.split())
print(decoded_text)

# 二进制
binary_str = '01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100'
text = ''.join(chr(int(b, 2)) for b in binary_str.split(' '))
print(text)
