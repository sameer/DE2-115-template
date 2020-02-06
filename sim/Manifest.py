action = "simulation"
sim_tool = "modelsim"
sim_top = "DE2_115_TOP_TB"

sim_post_cmd = "vsim -novopt -do ./vsim.do -c DE2_115_TOP_TB"

modules = {
  "local" : [ "../testbench/" ],
}
