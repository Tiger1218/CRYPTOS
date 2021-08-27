enc_example = "username=AAAAAA;is_admin=0;user_id=mss2020_0;\x07\x07\x07\x07\x07\x07\x07"
plainblocks = [enc_example[i * 16:i * 16 + 16] for i in range(len(enc_example) // 16)]
print(plainblocks)