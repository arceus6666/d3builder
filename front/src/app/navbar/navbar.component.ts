import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  @Input() tree: Array<string>;
  public _0: string;
  public _1: Array<string>;
  public _last: string;
  public lowertree: Array<string>;
  constructor(
    private _router: Router
  ) { }

  ngOnInit() {
    console.log(this.tree)
    this.lowertree = this.tree.map(e => e.toLowerCase());
    this._0 = this.tree.shift();
    this._last = this.tree.pop();
  }

  navigate(i: number = 0) {
    const url = this.lowertree.slice(1, i + 1).join('/');
    console.log(url);
    this._router.navigateByUrl(url);
    // if (i === 0) {
    // } else {
    //   this._router.navigateByUrl([this._0, ...this.tree.slice(0, i + 1)].join('/'));
    // }
  }

}
