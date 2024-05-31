;----------------------------------------------------------------------------------
; Problem Statement:-
;----------------------------------------------------------------------------------
;   Design a system to open and close a gate automatically based on vehicle
;   detection using sensors connected to port 20H. The gate should open when
;   a vehicle is detected and close when no vehicle is detected.
;
;   --------Assume, bit 0 of the input port 20H indicates vehicle detection
;   (1 = vehicle present, 0 = no vehicle) and port 21H controls the gate 
;   (01H = open gate, 00H = close gate).---------
;----------------------------------------------------------------------------------

#ORG 3000H

; to loop back to start
start:

    ; read sensor data from port 20H
    IN 20H

    ; check if bit 0 (D0) is set (vehicle detected)
    ANI 01H

    ; if D0 is set, jump to open_gate
    JNZ open_gate

    ; if D0 is not set, jump to close_gate
    JMP close_gate

; defining the label to open the gate
open_gate:

    ; move 01H to accumulator (open gate command)
    MVI A, 01H

    ; send the open gate command to port 21H
    OUT 21H

    ; go back to start
    JMP start

; defining the label to close the gate
close_gate:

    ; move 00H to accumulator (close gate command)
    MVI A, 00H

    ; send the close gate command to port 21H
    OUT 21H

    ; go back to start
    JMP start

HLT

;----------------------------------------------------------------------------------
