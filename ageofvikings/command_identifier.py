from command import *
from command_list import *

class CommandIdentifier(object):
    
    ''' Identifica e trata o comando digitado pelo usuário '''

    def __init__(self):
        self.words = []
        self.lineInput = ''
        self.command = None
        self.commandList = CommandList()

    def idCommand(self):
        self.lineInput = input(str("O que você faz? "))
        self.words = self.lineInput.lower().lstrip().split(' ', 1)
        self.words[0] = self.commandList.isValid2(self.words[0])
        if(self.words[0] != None):
            if (len(self.words) == 2):
                self.words[1].lower().lstrip()
                self.command = Command(self.words[0], self.words[1])
                return self.command
            elif(len(self.words) == 1):
                self.command = Command(self.words[0], None)
                return self.command
        else:
            return None

    def getCommands(self):
        return self.commandList.getCommandList()

    def getCommandsString(self):
        commandString = ''
        for command in self.commandList.getCommandList():
            commandString += ' ' + command
        return 'Comandos disponíveis: ' + commandString

    def getOneWords(self):
        return self.commandList.getOneWordCommands()
