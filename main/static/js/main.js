/**
 * Gets the current status of the collapsable element in the company section
 * of the page. Then modify the string and icon of the trigger button and string
 *
 * @param {string}  row  Row number of the company being selected
 * @return None
 */
function footerIcon(row){
    let triggerButton = document.getElementById("collapse"+row+"-trigger");
    let triggerIcon = document.getElementById("collapse"+row+"-icon");
    let isCollapsed = $("#collapse"+row).is(':hidden')

    if (isCollapsed){
      triggerButton.innerHTML = "Close"
      triggerIcon.setAttribute("d","M7.776 5.553a.5.5 0 0 1 .448 0l6 3a.5.5 0 1 1-.448.894L8 6.56 2.224 9.447a.5.5 0 1 1-.448-.894l6-3z")
      
    }else{
      triggerButton.innerHTML = "View Details"
      triggerIcon.setAttribute("d", "M1.553 6.776a.5.5 0 0 1 .67-.223L8 9.44l5.776-2.888a.5.5 0 1 1 .448.894l-6 3a.5.5 0 0 1-.448 0l-6-3a.5.5 0 0 1-.223-.67z");
    }
    
  }