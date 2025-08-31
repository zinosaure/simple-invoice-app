import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route, Outlet, Link } from "react-router-dom";
import * as bs from 'react-bootstrap';

const HOSTNAME = window.location.host;

function MenuItem() {
    return (
        <bs.Card>
            <bs.Card.Header>
                <i className="fa-solid fa-bars me-2"></i> Menu
            </bs.Card.Header>
            <bs.ListGroup variant="flush">
                <bs.ListGroup.Item>
                    <i className="fa-solid fa-users me-2"></i>
                    <Link to="/">
                        Invoices
                    </Link>
                </bs.ListGroup.Item>
                <bs.ListGroup.Item>
                    <i className="fa-solid fa-users me-2"></i>
                    <Link to="/invoice">
                        Invoice
                    </Link>
                </bs.ListGroup.Item>
            </bs.ListGroup>
        </bs.Card>
    );
}

function Dashboard() {
    return (
        <>
            <bs.Container className="mt-4">
                <bs.Card bg="dark" text="white">
                    <bs.Card.Body>
                        <bs.Navbar.Brand href="/">
                            <img className="logo" src="/public/images/horizontal-white.svg" />
                        </bs.Navbar.Brand>
                    </bs.Card.Body>
                </bs.Card>
            </bs.Container>
            <bs.Container className="mt-4">
                <bs.Row>
                    <bs.Col md="3">
                        <MenuItem />
                    </bs.Col>
                    <bs.Col>
                        <bs.Card>
                            <bs.Card.Body>
                                <Outlet />
                            </bs.Card.Body>
                        </bs.Card>
                    </bs.Col>
                </bs.Row>
            </bs.Container>
            <bs.Container className="my-4">
                <bs.Card>
                    <bs.Card.Body></bs.Card.Body>
                </bs.Card>
            </bs.Container>
        </>
    );
}

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Dashboard />}>
                    <Route index element={<ListInvoices />} />
                    <Route path="invoice" element={<CreateInvoice />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

const root = createRoot(document.getElementById("app"));
root.render(<App />);

const providers = [
    {
        id: 1,
        name: "Ethan Ross",
        street_num: 30,
        street_name: "Blvd. St Jean",
        postal_code: 95022,
        city: "Cergy-Pontoise",
        state: "Ile-de-France",
        siren: "952 5211 344",
        email: "ethan.ross@example.mail"
    },
];
const recipients = [
    {
        id: 1,
        name: "Facebook SAS",
        street_num: 19,
        street_name: "Rue Jean Jaurès",
        postal_code: 75001,
        city: "Paris",
        state: "Ile-de-France",
        siren: "753 2552 562",
        email: "invoice@facebook.com",
        contract: "Facebook-082025",
    },
    {
        id: 2,
        name: "Google Inc.",
        street_num: 56,
        street_name: "Avenue de Lyon",
        postal_code: 78005,
        city: "Versailles",
        state: "Ile-de-France",
        siren: "780 0545 123",
        email: "invoice@google.com",
        contract: "GG-963-58888",
    },
];

function load_id(id, items) {
    for (const i in items)
        if (items[i].id == id)
            return items[i];

    return {};
}

function CreateInvoice() {
    const items = [
        {
            id: 1,
            quantity: 20,
            title: "Prestations (TJM)",
            sub_title: "du 01/08 au 29/08",
            unit_price: 450,
            tax_rate: 0
        },
        {
            id: 2,
            quantity: 20,
            title: "Frais paiement anticipé",
            sub_title: "du 01/08 au 29/08",
            unit_price: -13.50,
            tax_rate: 0
        },
    ];
    let total_ht = 0;
    let total_tax = 0;

    return <>
        <h1 className="mb-4">
            <bs.Row className="mb-1">
                <bs.Col xs="1">
                    <bs.Button
                        type="button"
                        variant="outline-secondary"
                        className="h-100"
                        onClick={() => POP.close()}
                    >
                        <i className="fa-solid fa-pen"></i>
                    </bs.Button>
                </bs.Col>
                <bs.Col xs="11">
                    Facture #002
                </bs.Col>
            </bs.Row>
        </h1>
        <div className="row mb-2">
            <div className="col-6">
                <h6>
                    Prestataire:
                </h6>
                <CreateInvoice.Provider item={load_id(1, providers)} />
            </div>
            <div className="col-6 text-end">
                <h6>
                    Destinataire:
                </h6>
                <CreateInvoice.Recipient item={load_id(1, recipients)} />
            </div>
        </div>
        <div className="mb-4">
            <bs.Row className="mb-1">
                <bs.Col xs="1">
                    <bs.Button
                        type="button"
                        variant="outline-secondary"
                        className="h-100"
                        onClick={() => POP.close()}
                    >
                        <i className="fa-solid fa-pen"></i>
                    </bs.Button>
                </bs.Col>
                <bs.Col xs="11">
                    <div>Date de facture: <b>29/08/2025</b></div>
                    <div>Echéance de paiement: <b>29/08/2025</b></div>
                </bs.Col>
            </bs.Row>
            <bs.Row>
                <bs.Col xs="1">
                    <bs.Button
                        type="button"
                        variant="outline-secondary"
                        className="h-100"
                        onClick={() => POP.close()}
                    >
                        <i className="fa-solid fa-pen"></i>
                    </bs.Button>
                </bs.Col>
                <bs.Col xs="11">
                    <div>Device: <b>Euro (€)</b></div>
                    <div>Mode de règlement: <b>Virement bancaire</b></div>
                    <div>IBAN: <b>FR76 0000 1111 2222 3333 4444 555</b></div>
                    <div>BIC/SWIFT: <b>BNKFCTF01</b></div>
                </bs.Col>
            </bs.Row>
        </div>
        <div className="mb-4">
            <div className="table-responsive">
                <table className="table table-striped table-bordered">
                    <thead>
                        <tr>
                            <th width="1%" scope="col" className="text-uppercase"></th>
                            <th width="2%" scope="col" className="text-uppercase">Qté</th>
                            <th width="34%" scope="col" className="text-uppercase">Description</th>
                            <th width="24%" scope="col" className="text-uppercase text-end">Prix unitaire HT</th>
                            <th width="15%" scope="col" className="text-uppercase text-end">Taux TVA</th>
                            <th width="21%" scope="col" className="text-uppercase text-end">Prix total HT</th>
                        </tr>
                    </thead>
                    <tbody className="table-group-divider">
                        {items.map((item) => {
                            total_ht += item.quantity * item.unit_price;
                            return <CreateInvoice.Product item={item} />
                        })}
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="6" className="text-center">
                                <bs.Button
                                    type="button"
                                    variant="secondary"
                                    className="w-25"
                                    onClick={() => POP.close()}
                                >
                                    <i className="fa-solid fa-plus"></i>
                                </bs.Button>
                            </td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <div className="row">
                <div className="col-6"></div>
                <div className="col-6">
                    <table className="table table-striped table-bordered">
                        <tbody className="table-group-divider">
                            <tr>
                                <td width="55%" className="text-end">Total HT</td>
                                <td width="45%" className="text-end">{total_ht} €</td>
                            </tr>
                            <tr>
                                <td className="text-end">Total TVA</td>
                                <td className="text-end">{total_tax} €</td>
                            </tr>
                            <tr>
                                <th scope="row" className="text-uppercase text-end fw-bold">
                                    Total TTC</th>
                                <td className="text-end fw-bold">{total_ht + total_tax} €</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div className="text-center small">
            <bs.Row>
                <bs.Col xs="1">
                    <bs.Button
                        type="button"
                        variant="outline-secondary"
                        className="h-100"
                        onClick={() => POP.close()}
                    >
                        <i className="fa-solid fa-pen"></i>
                    </bs.Button>
                </bs.Col>
                <bs.Col xs="11">
                    En cas de retard, une pénalité au taux annuel de 5 % sera appliquée, à laquelle
                    s'ajoutera une indemnité forfaitaire pour frais de recouvrement de 40 €
                    TVA non applicable, art. 293B du CGI.
                </bs.Col>
            </bs.Row>
        </div>
    </>
};


CreateInvoice.Provider = ({ item }) => {
    return (
        <bs.Row>
            <bs.Col xs="2">
                <bs.Button
                    type="button"
                    variant="outline-secondary"
                    className="h-100"
                    onClick={() => POP.close()}
                >
                    <i className="fa-solid fa-pen"></i>
                </bs.Button>
            </bs.Col>
            <bs.Col xs="10">
                <address className="mb-0">
                    <b>{item.name}</b>
                    <br />
                    {item.street_num}, {item.street_name},
                    <br />
                    {item.postal_code}, {item.city}, {item.state}
                    <br />
                    Siren: <b>{item.siren}</b>
                    <br />
                    Email: <b>{item.email}</b>
                </address>
            </bs.Col>

        </bs.Row>
    );
};

CreateInvoice.Recipient = ({ item }) => {
    return (
        <bs.Row className="mb-3">
            <bs.Col xs="10">
                <address className="mb-0">
                    <b>{item.name}</b>
                    <br />
                    {item.street_num}, {item.street_name},
                    <br />
                    {item.postal_code}, {item.city}, {item.state}
                    
                    <br />
                    Siren: <b>{item.siren}</b>
                    <br />
                    Email: <b>{item.email}</b>
                    <br />
                    Contrat: <b>{item.contract}</b>
                </address>
            </bs.Col>
            <bs.Col xs="2">
                <bs.Button
                    type="button"
                    variant="outline-secondary"
                    className="h-100"
                    onClick={() => POP.close()}
                >
                    <i className="fa-solid fa-pen"></i>
                </bs.Button>
            </bs.Col>
        </bs.Row>
    );
};

CreateInvoice.Product = ({ item }) => {
    return (
        <tr>
            <td>
                <bs.Button
                    type="button"
                    variant="outline-secondary"
                    className="h-100"
                    onClick={() => POP.close()}
                >
                    <i className="fa-solid fa-pen"></i>
                </bs.Button>
            </td>
            <td className="fw-bold text-end">{item.quantity}</td>
            <td>
                <div className="fw-bold">{item.title}</div>
                <div className="small">{item.sub_title}</div>
            </td>
            <td className="text-end">{item.unit_price} €</td>
            <td className="text-end">{item.tax_rate} %</td>
            <td className="text-end">{item.unit_price * item.quantity} €</td>
        </tr>
    );
}

function ListInvoices() {
    return <h1>List invoice</h1>
};
