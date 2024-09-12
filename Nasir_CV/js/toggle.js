function toggle(whichLayer)
{
var style2;

if (document.getElementById)
{
// this is the way the standards work
 style2 = document.getElementById(whichLayer).style;
//style2.display = style2.display? "":"block";


}
else if (document.all)
{
// this is the way old msie versions work
var style2 = document.all[whichLayer].style;

}
else if (document.layers)
{
// this is the way nn4 works
var style2 = document.layers[whichLayer].style;

}
if(style2.display == "none")
			{
				style2.display = "";
				
				return;
			}
			
			else
			{
				style2.display = "none";
				
				return;
			}
alert(style2.display);
}
