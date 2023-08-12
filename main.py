import pandas as pd
import re

# Define the data string to parse. Replace this with your own data.
data = """(1) Team 9 - Cooper Kupp (LAR - WR) - $64
(2) Team 13 - Justin Jefferson (Min - WR) - $78
(3) Team 11 - Jonathan Taylor (Ind - RB) - $59
(4) solomon h - Christian McCaffrey (SF - RB) - $74
(5) Team 9 - Ja'Marr Chase (Cin - WR) - $75
(6) solomon h - Austin Ekeler (LAC - RB) - $64
(7) Team 11 - Tyreek Hill (Mia - WR) - $60
(8) matthew - Josh Jacobs (LV - RB) - $49
(9) Michael - Bijan Robinson (Atl - RB) - $60
(10) Bob - Travis Kelce (KC - TE) - $61
(11) matthew - Nick Chubb (Cle - RB) - $60
(12) Team 14 - Stefon Diggs (Buf - WR) - $53
(13) Mike - Saquon Barkley (NYG - RB) - $57
(14) Mike - Tony Pollard (Dal - RB) - $55
(15) matthew - Tee Higgins (Cin - WR) - $35
(16) Michael - CeeDee Lamb (Dal - WR) - $50
(17) Sutton - Amon-Ra St. Brown (Det - WR) - $44
(18) Michael - Derrick Henry (Ten - RB) - $55
(19) solomon h - Davante Adams (LV - WR) - $50
(20) Team 14 - Garrett Wilson (NYJ - WR) - $43
(21) Bob - Rhamondre Stevenson (NE - RB) - $43
(22) Nick - A.J. Brown (Phi - WR) - $50
(23) Team 10 - Jaylen Waddle (Mia - WR) - $41
(24) FernandoS - Breece Hall (NYJ - RB) - $37
(25) matthew - Najee Harris (Pit - RB) - $35
(26) Sutton - DeVonta Smith (Phi - WR) - $37
(27) Sutton - Chris Olave (NO - WR) - $36
(28) Team 10 - Jalen Hurts (Phi - QB) - $32
(29) Sutton - Travis Etienne Jr. (Jax - RB) - $33
(30) Team 11 - Aaron Jones (GB - RB) - $30
(31) Mike - Patrick Mahomes (KC - QB) - $31
(32) Sutton - Joe Mixon (Cin - RB) - $31
(33) FernandoS - DK Metcalf (Sea - WR) - $27
(34) Team 13 - Josh Allen (Buf - QB) - $27
(35) Team 11 - Amari Cooper (Cle - WR) - $22
(36) FernandoS - Keenan Allen (LAC - WR) - $20
(37) FernandoS - Mark Andrews (Bal - TE) - $25
(38) Nick - T.J. Hockenson (Min - TE) - $24
(39) Team 10 - Jahmyr Gibbs (Det - RB) - $24
(40) Team 13 - J.K. Dobbins (Bal - RB) - $22
(41) Team 10 - Kenneth Walker III (Sea - RB) - $20
(42) Michael - Miles Sanders (Car - RB) - $21
(43) Team 10 - Deebo Samuel (SF - WR) - $21
(44) Nick - Cam Akers (LAR - RB) - $20
(45) Team 12 - Calvin Ridley (Jax - WR) - $16
(46) Team 10 - Dameon Pierce (Hou - RB) - $19
(47) Nick - Joe Burrow (Cin - QB) - $17
(48) Nick - Tyler Lockett (Sea - WR) - $16
(49) Team 9 - Lamar Jackson (Bal - QB) - $14
(50) Team 11 - Alexander Mattison (Min - RB) - $17
(51) Team 13 - Drake London (Atl - WR) - $14
(52) Team 12 - George Kittle (SF - TE) - $14
(53) Team 13 - Dallas Goedert (Phi - TE) - $10
(54) Team 13 - Terry McLaurin (Was - WR) - $13
(55) Team 12 - James Conner (Ari - RB) - $10
(56) Mike - Chris Godwin (TB - WR) - $13
(57) FernandoS - DJ Moore (Chi - WR) - $11
(58) Team 14 - David Montgomery (Det - RB) - $9
(59) Team 12 - Jerry Jeudy (Den - WR) - $12
(60) Bob - DeAndre Hopkins (Ten - WR) - $12
(61) Sutton - Skyy Moore (KC - WR) - $4
(62) Team 9 - Christian Watson (GB - WR) - $9
(63) Mike - Diontae Johnson (Pit - WR) - $9
(64) Bob - Brandon Aiyuk (SF - WR) - $10
(65) Bob - Isiah Pacheco (KC - RB) - $8
(66) Team 9 - Kyle Pitts (Atl - TE) - $6
(67) Team 12 - Justin Fields (Chi - QB) - $9
(68) Team 14 - Michael Pittman Jr. (Ind - WR) - $9
(69) FernandoS - Rachaad White (TB - RB) - $7
(70) Bob - Trevor Lawrence (Jax - QB) - $7
(71) Bob - Dalvin Cook (Min - RB) - $7
(72) Bob - Justin Herbert (LAC - QB) - $7
(73) Team 12 - Mike Williams (LAC - WR) - $7
(74) matthew - Mike Evans (TB - WR) - $6
(75) matthew - Pat Freiermuth (Pit - TE) - $6
(76) Bob - Dak Prescott (Dal - QB) - $5
(77) FernandoS - Christian Kirk (Jax - WR) - $6
(78) Nick - Rashaad Penny (Phi - RB) - $7
(79) FernandoS - D'Andre Swift (Phi - RB) - $4
(80) Bob - Darren Waller (NYG - TE) - $7
(81) Team 14 - Evan Engram (Jax - TE) - $4
(82) Team 13 - Javonte Williams (Den - RB) - $5
(83) Bob - San Francisco (SF - DEF) - $3
(84) Team 9 - Brian Robinson (Was - RB) - $4
(85) Michael - Damien Harris (Buf - RB) - $3
(86) Team 12 - Tua Tagovailoa (Mia - QB) - $4
(87) Team 10 - Marquise Brown (Ari - WR) - $5
(88) Team 9 - Jahan Dotson (Was - WR) - $5
(89) Team 11 - Deshaun Watson (Cle - QB) - $3
(90) Sutton - Daniel Jones (NYG - QB) - $3
(91) Team 9 - AJ Dillon (GB - RB) - $4
(92) Team 14 - Alvin Kamara (NO - RB) - $3
(93) Bob - Dallas (Dal - DEF) - $3
(94) Team 10 - Greg Dulcich (Den - TE) - $2
(95) Mike - David Njoku (Cle - TE) - $3
(96) Mike - Khalil Herbert (Chi - RB) - $3
(97) Team 13 - Philadelphia (Phi - DEF) - $2
(98) Team 10 - Geno Smith (Sea - QB) - $3
(99) Sutton - New York (NYJ - DEF) - $2
(100) Team 14 - Anthony Richardson (Ind - QB) - $3
(101) Team 10 - George Pickens (Pit - WR) - $3
(102) Bob - Gabe Davis (Buf - WR) - $4
(103) Sutton - Chigoziem Okonkwo (Ten - TE) - $2
(104) Team 9 - Kirk Cousins (Min - QB) - $2
(105) Bob - James Cook (Buf - RB) - $4
(106) solomon h - Jamaal Williams (NO - RB) - $1
(107) Team 9 - Buffalo (Buf - DEF) - $2
(108) Nick - New England (NE - DEF) - $2
(109) Michael - Cole Kmet (Chi - TE) - $2
(110) Mike - Samaje Perine (Den - RB) - $3
(111) Team 13 - Justin Tucker (Bal - K) - $2
(112) Team 12 - Denver (Den - DEF) - $2
(113) FernandoS - Baltimore (Bal - DEF) - $2
(114) FernandoS - Aaron Rodgers (NYJ - QB) - $2
(115) Team 9 - Elijah Moore (Cle - WR) - $3
(116) Nick - Jordan Addison (Min - WR) - $2
(117) Sutton - Harrison Butker (KC - K) - $2
(118) Nick - Jared Goff (Det - QB) - $2
(119) Bob - Daniel Carlson (LV - K) - $4
(120) Sutton - Treylon Burks (Ten - WR) - $2
(121) Team 9 - Evan McPherson (Cin - K) - $1
(122) Team 10 - Miami (Mia - DEF) - $1
(123) Team 11 - Sam LaPorta (Det - TE) - $1
(124) Team 12 - Antonio Gibson (Was - RB) - $2
(125) FernandoS - Jaxon Smith-Njigba (Sea - WR) - $2
(126) Team 14 - Tyler Bass (Buf - K) - $2
(127) Mike - Kansas City (KC - DEF) - $1
(128) FernandoS - Younghoe Koo (Atl - K) - $1
(129) Team 12 - Rashod Bateman (Bal - WR) - $3
(130) Nick - Jake Elliott (Phi - K) - $1
(131) Team 9 - Elijah Mitchell (SF - RB) - $2
(132) matthew - Russell Wilson (Den - QB) - $1
(133) solomon h - Kadarius Toney (KC - WR) - $1
(134) Team 9 - Gerald Everett (LAC - TE) - $1
(135) Team 10 - Jake Moody (SF - K) - $1
(136) Team 11 - Cincinnati (Cin - DEF) - $1
(137) Team 12 - Jason Myers (Sea - K) - $1
(138) Mike - Brandin Cooks (Dal - WR) - $2
(139) Team 14 - Washington (Was - DEF) - $1
(140) Mike - Nick Folk (NE - K) - $1
(141) FernandoS - Dalton Schultz (Hou - TE) - $1
(142) Team 14 - Courtland Sutton (Den - WR) - $2
(143) Nick - Nico Collins (Hou - WR) - $2
(144) Team 10 - Zach Charbonnet (Sea - RB) - $2
(145) matthew - Tampa Bay (TB - DEF) - $1
(146) solomon h - Tyler Higbee (LAR - TE) - $1
(147) Team 9 - Pittsburgh (Pit - DEF) - $1
(148) Team 10 - Dalton Kincaid (Buf - TE) - $1
(149) Team 11 - Jason Sanders (Mia - K) - $1
(150) Team 14 - Tyler Allgeier (Atl - RB) - $2
(151) Team 13 - Jakobi Meyers (LV - WR) - $2
(152) Team 14 - Michael Thomas (NO - WR) - $2
(153) Mike - Kenneth Gainwell (Phi - RB) - $2
(154) FernandoS - Derek Carr (NO - QB) - $1
(155) Team 13 - JuJu Smith-Schuster (NE - WR) - $2
(156) Team 12 - Quentin Johnston (LAC - WR) - $2
(157) Sutton - D'Onta Foreman (Chi - RB) - $1
(158) matthew - Matt Gay (Ind - K) - $1
(159) solomon h - Matthew Stafford (LAR - QB) - $1
(160) Team 10 - Green Bay (GB - DEF) - $1
(161) Team 11 - Odell Beckham Jr. (Bal - WR) - $1
(162) Nick - Jerick McKinnon (KC - RB) - $2
(163) Team 13 - Jeff Wilson Jr. (Mia - RB) - $2
(164) Team 14 - Mike Gesicki (NE - TE) - $1
(165) Mike - Juwan Johnson (NO - TE) - $1
(166) FernandoS - Carolina (Car - DEF) - $1
(167) Michael - Jameson Williams (Det - WR) - $1
(168) Nick - Allen Lazard (NYJ - WR) - $1
(169) Sutton - Irv Smith Jr. (Cin - TE) - $1
(170) matthew - Zay Flowers (Bal - WR) - $1
(171) solomon h - New Orleans (NO - DEF) - $1
(172) Team 11 - Tyler Boyd (Cin - WR) - $1
(173) Team 12 - Jaylen Warren (Pit - RB) - $1
(174) Team 13 - Dawson Knox (Buf - TE) - $1
(175) Team 14 - Brock Purdy (SF - QB) - $1
(176) Mike - Kenny Pickett (Pit - QB) - $1
(177) Michael - Jordan Love (GB - QB) - $1
(178) Nick - Trey McBride (Ari - TE) - $1
(179) Sutton - Ryan Tannehill (Ten - QB) - $1
(180) matthew - Darnell Mooney (Chi - WR) - $1
(181) solomon h - Brandon McManus (Jax - K) - $1
(182) Team 11 - Ezekiel Elliott (Dal - RB) - $1
(183) Team 12 - Taysom Hill (NO - TE) - $1
(184) Team 13 - Sam Howell (Was - QB) - $1
(185) Team 14 - Detroit (Det - DEF) - $1
(186) Mike - Los Angeles (LAC - DEF) - $1
(187) Michael - Cleveland (Cle - DEF) - $1
(188) Nick - Jacksonville (Jax - DEF) - $1
(189) Sutton - Indianapolis (Ind - DEF) - $1
(190) matthew - Devin Singletary (Hou - RB) - $1
(191) solomon h - Raheem Mostert (Mia - RB) - $1
(192) Team 11 - Hayden Hurst (Car - TE) - $1
(193) Team 12 - Riley Patterson (Det - K) - $1
(194) Team 13 - Los Angeles (LAR - DEF) - $1
(195) Michael - Greg Joseph (Min - K) - $1
(196) matthew - Tyler Conklin (NYJ - TE) - $1
(197) solomon h - Adam Thielen (Car - WR) - $1
(198) Team 11 - Baker Mayfield (TB - QB) - $1
(199) Michael - Kendre Miller (NO - RB) - $1
(200) matthew - Kyler Murray (Ari - QB) - $1
(201) solomon h - Clyde Edwards-Helaire (KC - RB) - $1
(202) Team 11 - Greg Zuerlein (NYJ - K) - $1
(203) Michael - Rondale Moore (Ari - WR) - $1
(204) matthew - Robbie Gould (SF - K) - $1
(205) solomon h - Luke Musgrave (GB - TE) - $1
(206) Michael - Zach Ertz (Ari - TE) - $1
(207) solomon h - Desmond Ridder (Atl - QB) - $1
(208) Michael - Bryce Young (Car - QB) - $1
(209) solomon h - Seattle (Sea - DEF) - $1
(210) Michael - Graham Gano (NYG - K) - $1"""

# Function to parse a single line of the data
# This uses a regular expression to match the expected format and extract the desired parts
def parse_line(line):
    match = re.match(r'\((\d+)\) (.*?) - (.*?) \((.*?) - (.*?)\) - \$(\d+)', line)
    if match:
        return match.groups()

# Define the column names for the DataFrame
columns = ['Order #', 'Manager', 'Player Name', 'Team', 'Position', 'Price']

# Use a list comprehension to apply the parse_line function to each line in the data
# The if statement ensures that only lines matching the expected format are included
data_list = [parse_line(line) for line in data.split("\n") if line]

# Create a DataFrame from the parsed data
df = pd.DataFrame(data_list, columns=columns)

# Define the path to the CSV file where the data will be saved
# Modify this to save to a different location
csv_file_path = 'parsed_data.csv'

# Save the DataFrame to the specified CSV file
df.to_csv(csv_file_path, index=False)

# Print a message indicating where the CSV file was saved
print(f"CSV file saved to {csv_file_path}")
