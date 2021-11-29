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