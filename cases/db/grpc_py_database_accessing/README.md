# grpc_py_database_accessing

## Usage
```python
# Get Example
data, stat = db.get('*', 'ask_tb', '')
if stat != 'ok':
    log.error(f'stat:{stat} data:{data}')
    return

# Insert Example
if (stat := db.insert('ask_tb', 'head, is_pub, sub, access_to_show, has_deadline, deadline, photo', req).status) != 'ok':
    log.error(stat)
    send_msg(log, bot, tid, DBERR, rmvKb())
    return

# Update Example
if (stat := db.update('ask_tb', f"cid=array[{cid}], res='{jsonb}', stat=TRUE", f"where id={adata['0'][0]}").status) != 'ok':
    log.error(stat)
    send_msg(log, bot, tid, DBERR, get_kb(log, DEFALTKB))
    return
```

## Build
- Proto
    ```bash
    make proto
    ```

## Run
```bash
make run
```

## Issues
- At `database_pb2_grpc.py` change import
    ```python
    import api.grpc.database_pb2 as database__pb2
    ```