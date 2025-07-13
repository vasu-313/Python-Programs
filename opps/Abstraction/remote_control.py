from abc import ABC, abstractmethod

# Abstract class
class Remote(ABC):   # Inherit from ABC
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

# Subclass TVRemote
class TVRemote(Remote):
    def on(self):
        print("TV is ON")
    def off(self):
        print("TV is OFF")

# Subclass ACRemote
class ACRemote(Remote):
    def on(self):
        print("AC is ON")
    def off(self):
        print("AC is OFF")   

remotes = [TVRemote(), ACRemote()]

for remote in remotes:
    remote.on()
    remote.off()

