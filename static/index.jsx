function Page(props) {
return(<div>

{props.message}

</div>);

}

ReactDOM.render(<Page message="hello world" />, document.getElementById("root"));