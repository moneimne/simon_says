#!/bin/sh

list=""
gamestate=1
score=0

while [ $gamestate -eq 1 ]; do
  
  sleep 2 
  
  newcolor=$RANDOM
  newcolor=$(($newcolor % 4))
  list="$list $newcolor"

  for x in $list; do
    if [ $x -eq 0 ]; then
      echo $x red
      # color red
    elif [ $x -eq 1 ]; then
      echo $x blue
      # color blue
    elif [ $x -eq 2 ]; then
      echo $x green
      # color green
    else
      echo $x yellow
      # color yellow
    fi

    sleep 1
  done

  for x in $list; do
    read y
    if [ $x -ne $y ]; then
      gamestate=0
      echo "You lose! Your score is $score"
      exit 0
    fi
  done

  score=$(($score + 1))
done
