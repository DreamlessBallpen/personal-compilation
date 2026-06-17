# Personal attempt at creating a Graph that can be unidirectional or bi-directional for some items.
# We are also attempting to make one that can contain weights in the edges, or if not specified, to automatically default to one as the weight value.

# I feel like, due to the unclear set of goals that we have, it's difficulto visualize how to proceed. Let's take a break.

class Status:
    def get_status(self):
        return "InProgress"
        
class ReturnCode:
    code_dict = {
        "00" : "NoIssues",
        "01" : "MainObjectiveNotDoneButNotUrgent",
        "02" : "UrgentIssue"
    }
        
class Graph(Status):
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, v):
        if v in self.adj_list.keys():
            print(f"{v} already in our vertices.")
            return ReturnCode.code_dict["01"]
            
        # Else, we add the vertices, and each vertex would have a key.
        self.adj_list[v] = []
        return ReturnCode.code_dict["00"]
        
    # TODO
    def add_edge(self, v1, v2, wt=1:float, bidirectional=True:bool, presence_prereq=False:bool):
        if presence_prereq:
            # Hard conditions
            pass
        else:
            # Code adjusts when it can
            pass
            
        
        
