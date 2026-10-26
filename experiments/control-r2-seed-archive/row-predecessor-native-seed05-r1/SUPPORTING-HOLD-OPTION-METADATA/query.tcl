# Metadata only. No project is created/opened and no design data is loaded.
package require ::quartus::project
puts "ASSIGNMENT_METADATA_BEGIN"
foreach name {TDC_AGGRESSIVE_HOLD_CLOSURE_EFFORT OPTIMIZE_HOLD_TIMING} {
    puts "NAME=$name"
    set status [catch {get_assignment_name_info $name} value]
    puts "TCL_CATCH_STATUS=$status"
    puts "VALUE_BEGIN"
    puts $value
    puts "VALUE_END"
}
puts "ASSIGNMENT_METADATA_END"
