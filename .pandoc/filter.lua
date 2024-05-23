function remove_class_from_element(elem, class_to_remove)
	if elem.classes then
	   for i, class in ipairs(elem.classes) do
	       if class == class_to_remove then
		  table.remove(elem.classes, i)
		  break
		end
	    end
	end
	return elem
end

function add_rss_icon(el)
  if el.classes:includes("hasrss") then
    -- Create an img element
    remove_class_from_element(el, "hasrss")
    local img = pandoc.RawInline('html', '<img src="syndicated-feed-icon.gif"> </img>')
    
    -- Append the img element after the current element
    return {el, img}
  end
  return el
end

return {
  { 
    Link = add_rss_icon,
  }
}
