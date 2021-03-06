from bge import logic
from .PlayerConstants import PlayerState

def start_fallState(self):
	self.grounded = False
	self.fallTime = 0.0
	# go to idle state
	self.rig.stopArmLayer()
	self.switchState(PlayerState.FALL_STATE)

def start_ladderState(self):
	# reset hud action text
	# logic.globalDict['PlayerHUD'].resetActionText()
	# set property
	self.suspendDynamics()
	self.grounded = False
	self.onLadder = True
	# reset state time
	self.stateTime = 0.0
	# get the ladder target and get origin
	ladder =  self.ladderData[0]
	obj_origin = None
	for obj in ladder.children:
		if ("ladder_origin" in obj.name):
			obj_origin = obj
	# after fin set pos and orient
	self.worldPosition[0] = obj_origin.worldPosition[0]
	self.worldPosition[1] = obj_origin.worldPosition[1]
	self.orientation = self.ladderData[0].orientation
	# set state
	self.switchState(PlayerState.WAITLADDER_STATE)

def start_pathFollowLevelState(self):
	# block movement
	self.stopMovement()
	# hud transition
	# logic.globalDict['PlayerHUD'].fadeOutToDisplayTransition()
	# swithc state
	self.switchState(PlayerState.PATH_FOLLOW_LEVEL_STATE)

def start_levelGapState(self):
	# stop any movement
	self.stopMovement()
	self.grounded = False
	# go to jump
	self.linearVelocity[2] += 10.0
	self.linearVelocity[1] += 1.5
	#self.suspendDynamics()
	# look at the gap
	self.setTrackOrient(self.levelManager.pathObject)
	# play jump to gap anim
	self.rig.playJumpSalto()
	# deactivate track player cam
	self.camManager.deactiveTrackPlayer()
	self.camManager.activeLookPlayer()
	# switch state
	self.switchState(PlayerState.LEVEL_GAP_STATE)

def start_firstLookView(self):
	self.orientManager.stopOrientation(self)
	self.stopMovement()
	self.camManager.camToFirstview()
	self.switchState(PlayerState.FIRST_LOOK_VIEW_STATE)
