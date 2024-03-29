import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';

import * as pages from '../pages/Pages';
import Layout from '../components/layout/Layout';

/* 
    App component handling routing
*/
console.log(pages)

const App = () => {
    return (
        <BrowserRouter>
            <Layout>
                <Route exact path="/" component={pages.Landing} />
                <Route path="/login" component={pages.Login} />
                <Route path="/signup" component={pages.SignUp} />
            </Layout>
        </BrowserRouter>
    );
};

export default App;