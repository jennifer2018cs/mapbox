function Page(props) {

return React.createElement(

"div",

null,

props.message

);

}

ReactDOM.render(React.createElement(Page, { message: "hello world" }), document.getElementById("root"));