describe('My first test', () => {

    it('Visits the app and confirms the title', () =>{
        // visit the site on liveserver
        cy.visit('http://127.0.0.1:5500/index.html#');
        // assert the title is correct
        cy.title().should('include', 'CleanCity: Waste Pickup Scheduler');
        cy.screenshot();
        });

    // assert that the navbar works
    // Click on each button and verify the URL changes accordingly
    it('Checks NavBar buttons', () => {
            // visit the site on liveserver
        cy.visit('http://127.0.0.1:5500/index.html');
        cy.get('#nav-menu').contains('Home').click();
        cy.url().should('include', '');
        cy.screenshot();

        cy.visit('http://127.0.0.1:5500/index.html');
        cy.get('#nav-menu').contains('login').click();
        cy.url().should('include', '#login');

        

    });
    });