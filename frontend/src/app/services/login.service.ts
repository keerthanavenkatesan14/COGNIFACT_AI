import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';


export interface LoginRequest {

  email: string;

  password: string;

}


export interface LoginUser {

  user_id: number;

  full_name: string;

  email: string;

  factory_id: number;

  factory_name: string;

  role_id: number;

  role: string;

}


export interface LoginResponse {

  message: string;

  token: string;

  user: LoginUser;

}


@Injectable({
  providedIn: 'root'
})


export class LoginService {

  private apiUrl =
    'http://localhost:5000/api';


  constructor(
    private http: HttpClient
  ) {}


  login(
    loginData: LoginRequest
  ): Observable<LoginResponse> {

    return this.http.post<LoginResponse>(
      `${this.apiUrl}/login`,
      loginData
    );

  }

}