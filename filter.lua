function add_rss_icon(el)
  if el.classes:includes("hasrss") then
    -- Create an img element
    local img = pandoc.RawInline('html', '<img src="public/syndicated-feed-icon.gif"> </img>')
    
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
