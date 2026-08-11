import { Injectable } from '@angular/core';

import {
  HttpClient
} from '@angular/common/http';

import {
  Observable
} from 'rxjs';


export interface RegisterRequest {

  company_name: string;

  industry: string;

  city: string;

  state: string;

  full_name: string;

  phone: string;

  email: string;

  password: string;

}


export interface RegisterResponse {

  message: string;

  user_id: number;

  factory_id: number;

}


@Injectable({
  providedIn: 'root'
})


export class RegisterService {

  private apiUrl =
    'http://localhost:5000/api';


  constructor(
    private http: HttpClient
  ) {}


  register(
    registerData: RegisterRequest
  ): Observable<RegisterResponse> {

    return this.http.post<RegisterResponse>(

      `${this.apiUrl}/register`,

      registerData

    );

  }

}