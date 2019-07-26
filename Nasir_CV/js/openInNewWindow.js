
var newwindow;

function openInNewWindow(url)
{
	newwindow=window.open(url, 'name','toolbar=1,location=1,scrollbars=1,resizable=1,directories=1,status=1,menubar=1');
	if (window.focus) 
	{
		newwindow.focus()
	}
}


