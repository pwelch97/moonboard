# Bluetooth monitoring

```
ssh -lpi raspi-moonboard sudo btmon
```

# DBUS Monitoring
```
ssh -lpi raspi-moonboard sudo dbus-monitor --system|less
```

# Logfiles
/var/log/moonboard_stdout.log
/var/log/moonboard_ble_stdout.log
```
ssh -lpi raspi-moonboard "tail -f /var/log/moonboard*"
```

# Resetting services
```
ssh -lpi raspi-moonboard "./moonboard/scripts/fix_startup.sh"
```


# Updating
ssh -lpi raspi-moonboard "cd moonboard ; git pull; cd install ; ./install.sh"
