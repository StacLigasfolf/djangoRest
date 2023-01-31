import React from 'react';
// import logo from './logo.svg';
import axios from 'axios';
import './App.css';
import AuthorList from './components/Author.js';
import BookList from "./components/Books";
import {HashRouter, Route} from 'react-router-dom';

class App extends React.Components{
    constructor(props) {
        super(props)

        const author1 = {id: 1, name: 'green', birthday_year: 1880}
        const author2 = {id: 2, name: 'greens', birthday_year: 1883}
        const authors = [author1, author2]


        const book1 = {id: 1, first_name: 'safta', author: author1}
        const book2 = {id: 2, first_name: 'freya', author: author2}
        const book3 = {id: 3, first_name: 'Collins', author: author1}
        const book4 = {id: 4, first_name: 'Push', author: author2}

        this.state = {
            'authors': authors,
            'books' : books,
        }
    }
    componentDidMount() {
        axios.get('http//127.0.0.1:8000/api/authors').then(response=>{
            const authors = response.data
            this.setState(
                {
                    'authors': authors
                }
            )
        }).catch(error => console.log(error))
    }
        
    render () {
        return (
            <div className='App'>
                <HashRouter>
                    <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}>
                <HashRouter/>

                <AuthorList authors={this.state.authors} />
                <BookList items={this.state.books}/>
            </div>
        )
    }
}

    

export default App;
