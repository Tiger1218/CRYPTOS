from Crypto.Util.number import *
p =  7049120988661090136959367990211624032671088374397430253722914704672269343351268486642692858477617370573493581346846411168539408811542592351582581576539221
q =  11595461299251293002401295606096202123601375776115430944343338141843770078346355504245510150744085418550473572002573306023521368183889972175846278163010889
c =  48425576447741107904942007362859939933300480519833273210397511573241220126734053813936424490872852942885069257318462762079636783871415500644717758273774268724488497979368196170897933989184449432995120246590652553995031347596620505647525475638040859263109628716173897321613612254357251120398449111747305089380

n = p * q
phi = (p - 1) * (q - 1)
print(long_to_bytes(pow(c,inverse(65537 , phi),n)))