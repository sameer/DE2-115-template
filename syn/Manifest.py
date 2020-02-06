target = "altera"
action = "synthesis"

syn_family = "CYCLONE IV"
syn_device = "EP4CE115"
syn_grade = "C7"
syn_package = "F29"
syn_top = "DE2_115_TOP"
syn_project = "lab2"
syn_tool = "quartus"

quartus_preflow = "../top/pinout.tcl"
quartus_postmodule = "../top/module.tcl"

modules = {
  "local" : [
    "../top"
  ],
}
