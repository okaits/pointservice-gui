#!/bin/bash
# /home/pi/PointService/rec.sh (P:$HOME/PointService/rec.sh) (R:record) (B:False(none)) (S:SEND, int)
echo "Program Running..."
cd $HOME/PointService-rc2/record/$SEND
oldpts=$(cat point)
cpts=$((${oldpts}-${SEND1}+1))
echo $cpts > point
echo $(date)": -"$SEND1"("$cpts"): Successfull(Changed)" >> log.log
cd ~/PointService-rc2
rm rank
$HOME/PointService-rc2/rank.sh
exit
