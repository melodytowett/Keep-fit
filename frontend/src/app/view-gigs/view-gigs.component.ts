import { Component, OnInit } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';


import { environment } from 'src/environments/environment';
import { Gig } from '../gig';

@Component({
  selector: 'app-view-gigs',
  templateUrl: './view-gigs.component.html',
  styleUrls: ['./view-gigs.component.css']
})
export class ViewGigsComponent implements OnInit {
  url: string = environment.API_URL ;
  gigs: Gig[];
  gig = Gig;

  constructor(private readonly http: HttpClient) {}

  ngOnInit(): void {


    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })};

    let response:any={}

    this.http.get(this.url, httpOptions).subscribe(data=>{
      response = data
      this.gigs = response

    })
  }

}
