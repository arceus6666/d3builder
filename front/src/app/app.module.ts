import { AppRoutingModule } from './app.routing';

import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ErrorComponent } from './error/error.component';
import { LoginComponent } from './login/login.component';
import { BuildComponent } from './build/build.component';
import { BannerComponent } from './banner/banner.component';
import { NavbarComponent } from './navbar/navbar.component';
import { DividerComponent } from './divider/divider.component';
import { ProfileComponent } from './profile/profile.component';
import { NotDoneComponent } from './not-done/not-done.component';
import { RegisterComponent } from './register/register.component';
import { BuildlistComponent } from './buildlist/buildlist.component';
import { BuildcreateComponent } from './buildcreate/buildcreate.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ErrorComponent,
    LoginComponent,
    BuildComponent,
    BannerComponent,
    NavbarComponent,
    DividerComponent,
    ProfileComponent,
    NotDoneComponent,
    RegisterComponent,
    BuildlistComponent,
    BuildcreateComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
