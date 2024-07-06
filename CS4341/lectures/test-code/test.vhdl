library IEEE; 
use IEEE.STD_LOGIC_1164.all; 
entity simplefunction is 
port (a, b, c: in STD_LOGIC; 
y: out STD_LOGIC); 
end; 
architecture synth of simplefunction is 
begin 
y <= ((not a) and (not b) and (not c)) or 
(a and (not b) and (not c)) or 
(a and (not b) and c); 
end;
