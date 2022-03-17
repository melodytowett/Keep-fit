import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewGigsComponent } from './view-gigs.component';

describe('ViewGigsComponent', () => {
  let component: ViewGigsComponent;
  let fixture: ComponentFixture<ViewGigsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewGigsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewGigsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
