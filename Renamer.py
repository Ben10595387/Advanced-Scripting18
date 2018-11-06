import maya.cmds as cmds

def RenameSelectedObject(input):
    SelectedObject = cmds.ls(sl = True)
    newarray = input.split('#')
    newarray = [newarray[0], newarray[len(newarray)-1]]
    print(newarray)  
    
    
RenameSelectedObject("Box_###_Geo")           
        #string $INPUT = `textField -query -text $newarray[0]`;
        #string $SUFFIX = `textField -query -text $newarray[1]`;        
        #int $begnumber = 1; //beginning number starting array.
        #$input = ($INPUT + "##" + $SUFFIX);
        #recount = size($input) - (size(INPUT) + size(SUFFIX));
        recount = size($input) - (size(newarray[0]) + size(SUFFIX[1]))
        #print("size1: " + size($input) + " size2: " + size($INPUT) + " suffixsize: " + size($SUFFIX) + "\n");
        #print($input + "\n");

        for($item in $SelectedObject)
        {
            string $PaddingNum;
            int $SelectedAmount = 0;

            for($i = 0; $i <= $begnumber; $i += 10)
            {
                $SelectedAmount++;
            }
            print ($recount);
            int $AmountRecount = $recount - $SelectedAmount;

            for($i = 0; $i < $AmountRecount; $i++)
            {
                $PaddingNum += "0";
            }

            $PaddingNum += $begnumber;
            $begnumber++;

            string $Reorder = $INPUT + "_" + $PaddingNum + "_" + $SUFFIX;
            rename $item $Reorder;
        }
    }
RenameSelectedObject(Box_Geo)
