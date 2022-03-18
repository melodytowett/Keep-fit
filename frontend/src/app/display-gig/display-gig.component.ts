import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router'

import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';


import { environment } from 'src/environments/environment';

import { DisplayGig } from '../display-gig';

@Component({
  selector: 'app-display-gig',
  templateUrl: './display-gig.component.html',
  styleUrls: ['./display-gig.component.css']
})
export class DisplayGigComponent implements OnInit {
  url: string = environment.API_URL+'display-gig/' ;
  displayGig: DisplayGig;

  id: any

  constructor(private route: ActivatedRoute, private readonly http: HttpClient) {}

  ngOnInit(): void {
    this.id = this.route.snapshot.paramMap.get('id')



    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })};

    let response:any={}

    this.http.get(this.url+this.id, httpOptions).subscribe(data=>{
      response = data
       this.displayGig= response
     

    })

  }

}
