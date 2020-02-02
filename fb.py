import facebook

access_token = "EAAAAAYsX7TsBAFOGZA7JpCmATAuA1NvhDLKPDY4T1EWrHZCNZADTaBu9FrlYO52hTZBEPDOioo9b8RZC8JGZB3CUwFSexbkdNZAEV9McpVt3rLyfSgFFdoRMsGUruthMDmdhZCX3RGNZATIpLCQto0g6UfGgKnwoZC5V52pblXOZBZBeF5SVLlwv2A9JHrXZBYmYiWZB9ZANgoZAjpfZBkXZAMPrXVViM0"

fb = facebook.GraphAPI(access_token)


class facebook:
    def post_on_wall(self, message):
        fb.put_object('me', 'feed', message=message)
