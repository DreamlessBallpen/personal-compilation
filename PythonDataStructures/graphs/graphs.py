# Personal attempt at creating a Graph that can be unidirectional or bi-directional for some items.
# We are also attempting to make one that can contain weights in the edges, or if not specified, to automatically default to one as the weight value.

# I feel like, due to the unclear set of goals that we have, it's difficult to visualize how to proceed.
# Still, take a break, but don't give up.

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
        
    def __str__(self):
        # [TESTED]
        
        if len(self.adj_list) == 0:
            return """ 
            ========= GRAPH =========
            No vertices in graph.
            =========================
            """
        else:
            text_to_return = ""
            
            text_to_return += "============ GRAPH ============"
            for k, v in self.adj_list.items():
                new_line = f"\n[{k}]: {v}"
                text_to_return += new_line
            text_to_return += "\n==============================="
            
            return text_to_return
    
    def add_vertex(self, v):
        if v in self.adj_list.keys():
            print(f"{v} already in our vertices.")
            return ReturnCode.code_dict["01"]
            
        # Else, we add the vertices, and each vertex would have a key.
        self.adj_list[v] = []
        return ReturnCode.code_dict["00"]
        
    # TODO
    def add_edge(self, v1, v2, wt:float=1, bidirectional:bool=True, presence_prereq:bool=False):
        assert wt > 0, "Edge weights cannot be negative."
        
        # Compile validation criteria first, make code simpler.
        v1_and_v2_available = not((not v1 in self.adj_list.keys()) or (not v2 in self.adj_list.keys()))
        
        # Evaluate code block "cases" for us to track here.
        
        # [CASE1] v1 and v2 exists, bidirectional, presence_prereq is True.
        
        # This evaluates what we pass into our 'switch' statement later.
        code_block_decision = 0
        if (v1_and_v2_available and bidirectional and presence_prereq):
            code_block_decision = 1
            
            
        # Actual steps.
        If code_block_decision == 1:
            # Add the links
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            # paused here, but continue soon!
            
        
        
        
