import pythonping
from multiprocessing import Pool
from cnc.command import Command, CommandType, CommandAnswer
from cnc.settings import DEFAULT_POOL_PROCSESES


class GetComputersCommand(Command):
    def __init__(self, command_id):
        super(GetComputersCommand, self).__init__(command_id)

    async def execute(self, agent_manager):
        try: 
            with open(r'computers.db', 'r') as computers_db:
                computers = computers_db.read()
        except IOError:
            computers = '[]'
            
        return GetComputersCommandAnswer(self.command_id, computers)

    def serialize(self):
        return {
            'commandId': self.command_id,
            'type': CommandType.GET_COMPUTERS.value,
        }

    @staticmethod
    def deserialize(data):
        return GetComputersCommand(command_id=data['commandId'])


class GetComputersCommandAnswer(CommandAnswer):
    def __init__(self, command_id, computers):
        super(GetComputersCommandAnswer, self).__init__(command_id) 
        self.computers = computers

    def serialize(self):
        return dict({
            'commandId': self.command_id,
            'type': CommandType.GET_COMPUTERS.value,
            'computers': self.computers
        })

    @staticmethod
    def deserialize(data):
        return GetComputersCommandAnswer(data['commandId'])