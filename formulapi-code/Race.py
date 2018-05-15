import time
### Enable logging ###
StartDetailedLoging()
StartUserLog()

### Wait for the lights ###
WaitForGo()

### Racing for 10 minutes ###
endTime = time.time() + 10 * 60
while time.time() < endTime:
	# Wait until we reach the first corner
	WaitForSeconds(20)
	ResetRace()
	print("yipee")
	# Wait until we reach the start / finish line
	WaitForSeconds(20)

### Wait for a few seconds ###

### Disable logging ###
EndDetailedLog()
EndUserLog()

### End of the race ###
FinishRace()
