for u in $(cat users.txt);
  do rpcclient -U "" 10.x.x.x -N \
  --command="lookupnames $u";
done | grep "User: 1"
