import fs  from 'node:fs';

const index =  fs.readFileSync('public/static/index.html', 'utf8', (err, data) => {
	if (err){
		console.error(err);
	}
    return data 
}) 


const myHeaders = new Headers();
myHeaders.append("Content-Type", "text/html; charset=utf-8");
const myOptions = { status: 200, 
	statusText: "SuperSmashingGreat!", 
	headers: myHeaders
};


const index_zh =  fs.readFileSync('public/static/index_zh.html', 'utf8', (err, data) => {
	if (err){
		console.error(err);
	}
    return data 
}) 


export default async (request, context) => {
	console.log("the accept-language header is: " + request.headers.get("accept-language"));
	var lang = request.headers.get("accept-language");
	if (!lang){
		return Response.json({
			statusCode: 200,
			statusText: "language unknown\n"})
	}
	if (lang.split(",")[0].substring(0,2) === "en" ){
		return new Response(index, myOptions)
	}
	else if (lang.split(",")[0].substring(0,2) === "zh"){
		return new Response(index_zh, myOptions)
	}
	else {
	return Response.json({
		statusCode:200
		})
	}
};
