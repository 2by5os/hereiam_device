set -x
export BLUETOOTH_DEVICE=hci0

export OGF="0x08"
export OCF="0x0008"
export IBEACONPROFIX="1E 02 01 1A 1A FF 4C 00 02 15"

export UUID="4a 4e ce 60 7e b0 11 e4 b4 a9 08 00 20 0c 9a 66"
export MAJOR="00 02"
export MINOR="00 01"
export POWER="C5 00"

sudo hciconfig $BLUETOOTH_DEVICE up
sudo hciconfig $BLUETOOTH_DEVICE noleadv
sudo hciconfig $BLUETOOTH_DEVICE noscan
sudo hciconfig $BLUETOOTH_DEVICE pscan
sudo hciconfig $BLUETOOTH_DEVICE leadv

sudo hcitool -i $BLUETOOTH_DEVICE cmd 0x08 0x0008 $IBEACONPROFIX $UUID $MAJOR $MINOR $POWER
sudo hcitool -i $BLUETOOTH_DEVICE cmd 0x08 0x0006 A0 00 A0 00 00 00 00 00 00 00 00 00 00 07 00
sudo hcitool -i $BLUETOOTH_DEVICE cmd 0x08 0x000a 01

chmod 777 /var/run/sdp
echo "complete"
